from flask import Flask, request, render_template

app = Flask(__name__)


def is_persian(text):
    for char in text:
        if '\u0600' <= char <= '\u06FF':
            return True
    return False


def verbal_analyze(code):
    global identifier
    if is_persian(code):
        return 'Error: Input value is Persion. Please write your code in english format.'

    tokens = []
    i = 0

    keywords = [
        'int', 'float', 'void', 'double', 'short', 'long', 'signed', 'unsigned',
        'enum', 'const', 'if', 'elif', 'else', 'while', 'switch', 'break',
        'continue', 'case', 'default', 'return', 'for', 'goto', 'do', 'main'
    ]

    symbols = [
        '(', ')', '{', '}', ';', '"', '//', '/*', '*/'
    ]

    operators = [
        '+', '-', '*', '/', '%', '=', '==', '!=', '&&', '||', '<', '>'
    ]

    enums = {}
    current_enum = None

    while i < len(code):
        char = code[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit():
            num = char
            i += 1
            while i < len(code) and (code[i].isdigit() or code[i] == '.'):
                num += code[i]
                i += 1
            tokens.append(('CONST', num))
            continue

        if char.isalpha() or char == '_':
            identifier = char
            i += 1
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                identifier += code[i]
                i += 1

            if current_enum is not None:
                enums[current_enum].append(identifier)
                tokens.append(('ENUM_VALUE', identifier))
            elif identifier in keywords:
                if identifier == 'enum':
                    current_enum = None
                tokens.append(('KEYWORD', identifier))
            else:
                tokens.append(('IDENTIFIER', identifier))
            continue

        if char == '{' and current_enum is None:
            current_enum = identifier
            enums[current_enum] = []
            tokens.append(('SYMBOL', char))
            i += 1
            continue
        if char == '}' and current_enum is not None:
            current_enum = None
            tokens.append(('SYMBOL', char))
            i += 1
            continue

        if code[i:i + 2] == '//':
            comment = ''
            i += 2
            while i < len(code) and code[i] != '\n':
                comment += code[i]
                i += 1
            tokens.append(('COMMENT_SINGLELINE', comment))
            continue

        if code[i:i + 2] == '/*':
            comment = ''
            i += 2
            while i < len(code) and code[i:i + 2] != '*/':
                comment += code[i]
                i += 1
            i += 2
            tokens.append(('COMMENT_MULTILINE', comment))
            continue

        for operator in operators:
            if code[i:i+len(operator)] == operator:
                tokens.append(('OPERATOR', operator))
                i += len(operator)
                break
        else:
            if char in symbols:
                tokens.append(('SYMBOL', char))
                i += 1
                continue

        print(f"Unexpected Character: {char}")
        i += 1

    return tokens


@app.route('/', methods=['GET', 'POST'])
def codeanalyzer():
    tokens = []
    error = None
    if request.method == 'POST':
        code = request.form['code']
        result = verbal_analyze(code)
        if isinstance(result, str):
            error = result
        else:
            tokens = result
    return render_template('index.html', tokens=tokens, error=error)


if __name__ == '__main__':
    app.run(debug=True)


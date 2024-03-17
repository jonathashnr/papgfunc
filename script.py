
# Função de primeira alta com closure
def validade_function(prompt, validate_type):
    err_message = 'Tipo de entrada inválido, a entrada deve ser do tipo: ' + str(validate_type)
    def validator():
        while True:
            func_input = input(prompt)
            try:
                func_input = validate_type(func_input)
                break
            except:
                print(err_message)
        return func_input
    return validator

# Outra função de alta ordem,
# mas agora com função lambda e list comprehension
def prog_function(tipo):
    if tipo == 'pa':
        return lambda r, e1, n: [e1 + i * r for i in range(n)]  # list comprehension e função lambda
    else:
        return lambda r, e1, n: [e1 * r ** i for i in range(n)] 

while True:
    while True:
        prog = input('Você quer calcular uma progressão aritimética(PA) ou uma progressão geométrica(PG)? ').lower()
        if prog == 'pa' or prog == 'pg':
            break
        else:
            print('Entrada inválida, as únicas entradas válidas são PA e PG.')
    validate_razao = validade_function('Qual é a razão da progressão? ', float)
    validate_e1 = validade_function('Qual é o valor do primeiro elemento? ', float)
    validate_n = validade_function('Quantos elementos deve ter a progressão? ', int)
    razao = validate_razao()
    e1 = validate_e1()
    n = validate_n()
    prog_func = prog_function(prog)
    prog_list = prog_func(razao,e1,n)
    print(prog_list)
    wanna_quit = input('Deseja calcular mais uma progressão? ').lower()
    if wanna_quit != 's' and wanna_quit != 'sim':
        break
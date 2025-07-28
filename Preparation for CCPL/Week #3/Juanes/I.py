from sys import stdin

def main():
    case = 1 
    
    for line in stdin:
        hello_word = line.strip()

        if hello_word == '#':
            break

        match hello_word:
            case 'HELLO':
                print(f'Case {case}: ENGLISH')
            case 'HOLA':
                print(f'Case {case}: SPANISH')
            case 'HALLO':
                print(f'Case {case}: GERMAN')
            case 'BONJOUR':
                print(f'Case {case}: FRENCH')
            case 'CIAO':
                print(f'Case {case}: ITALIAN')
            case 'ZDRAVSTVUJTE':
                print(f'Case {case}: RUSSIAN')
            case _:
                print(f'Case {case}: UNKNOWN')
        
        case += 1

if __name__ == '__main__':
    main()

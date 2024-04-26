#include <stdio.h>

int main() {
    char operador;
    double num1, num2, resultado;

    // Solicitar al usuario que ingrese el operador
    printf("Ingrese un operador (+, -, *, /): ");
    scanf("%c", &operador);

    // Solicitar al usuario que ingrese dos números
    printf("Ingrese dos numeros: ");
    scanf("%lf %lf", &num1, &num2);

    // Calcular el resultado basado en el operador ingresado
    switch (operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if (num2 != 0)
                resultado = num1 / num2;
            else {
                printf("Error: division por cero\n");
                return 1;
            }
            break;
        default:
            printf("Operador no valido\n");
            return 1;
    }

    // Imprimir el resultado
    printf("Resultado: %.2lf\n", resultado);

    return 0;
}

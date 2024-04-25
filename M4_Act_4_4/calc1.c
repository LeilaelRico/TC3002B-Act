#include <stdio.h>

int main() {
    float num1, num2;
    char operador;
    
    printf("Ingrese el primer número: ");
    scanf("%f", &num1);
    
    printf("Ingrese el segundo número: ");
    scanf("%f", &num2);
    
    printf("Ingrese el operador (+, -, *, /): ");
    scanf(" %c", &operador); // Espacio antes de %c para ignorar espacios en blanco
    
    switch (operador) {
        case '+':
            printf("Suma: %.2f\n", num1 + num2);
            break;
        case '-':
            printf("Resta: %.2f\n", num1 - num2);
            break;
        case '*':
            printf("Multiplicación: %.2f\n", num1 * num2);
            break;
        case '/':
            if (num2 != 0) {
                printf("División: %.2f\n", num1 / num2);
            } else {
                printf("No se puede dividir por cero.\n");
            }
            break;
        default:
            printf("Operador no válido.\n");
    }
    
    return 0;
}
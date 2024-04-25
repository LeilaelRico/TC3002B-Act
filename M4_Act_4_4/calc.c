#include <stdio.h>

int main() {
    float num1, num2;
    
    printf("Ingrese el primer número: ");
    scanf("%f", &num1);
    
    printf("Ingrese el segundo número: ");
    scanf("%f", &num2);
    
    printf("Suma: %.2f\n", num1 + num2);
    printf("Resta: %.2f\n", num1 - num2);
    printf("Multiplicación: %.2f\n", num1 * num2);
    
    // Verificamos si el segundo número no es cero para evitar la división por cero
    if (num2 != 0) {
        printf("División: %.2f\n", num1 / num2);
    } else {
        printf("No se puede dividir por cero.\n");
    }
    
    return 0;
}
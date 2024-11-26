#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef double element;

typedef struct StackType
{
    int top;
    element data[101];
}StackType;

void init(StackType* S)
{
    S-> top = -1;
}

int isEmpty(StackType* S)
{
    return S-> top == -1;
}

void push(StackType* S, element e)
{
    S-> top++;
    S-> data[S-> top] = e;
}

element pop(StackType* S)
{
    if(isEmpty(S))
        return -1;
    element e = S-> data[S-> top];
    S-> top--;
    return e;
}

double calculate(char str[], double value[])
{
    StackType S;
    init(&S);

    double op1, op2;
    int num;
    char c;

    int n = strlen(str);
    for(int i = 0; i < n; i++)
    {
        c = str[i];
        if(c >= 'A' && c <= 'Z')
        {
            num = c - 'A';
            push(&S, value[num]);
        }
        else if(c == '+' || c == '-' ||c == '*' ||c == '/')
        {
            op2 = pop(&S);
            op1 = pop(&S);

            switch (c)
            {
            case '+': push(&S, op1 + op2); break;
            case '-': push(&S, op1 - op2); break;
            case '*': push(&S, op1 * op2); break;
            case '/': push(&S, op1 / op2); break;
            }
        }
    }
    return pop(&S);
}

int main()
{
    int n;
    scanf("%d", &n);
    getchar();

    char str[101];
    fgets(str, 101, stdin);
    str[strcspn(str, "\n")] = 0;

    double* value = (double*)malloc(sizeof(double) * n);
    for(int i = 0; i < n; i++)
    {
        scanf("%lf", &value[i]);
    }
    printf("%.2f\n", (double)calculate(str, value));

    return 0;
}
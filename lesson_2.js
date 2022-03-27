// 1. 

var a = 1, b = 1, c, d;
c = ++a
console.log(c) // 2 (значение переменной а ++ увеличивает на 1)

d = b++
console.log(d) // 1 (Это постфиксный инкремент, поэтому возвращено значение, содержавшееся в переменной до её увеличения на 1)

c = (2+ ++a)
console.log(c) // 5 (в переменной а у нас уже значение 2, ++а увеличт еще на 1 и прибавим к 2 получаем 5)

d = (2+ b++)
console.log(d) // 4 (в переменной b у нас значение 2, и до ее увелечения мы к ней прибавляем 2 получаем 4)

console.log(a) // 3 
console.log(b) // 3 

// 2. Чему равен x?

var a = 2
var x = 1 + (a *= 2)
console.log(`X:`, x) // x = 5

// 3. Объявить две целочисленные переменные — a и b и задать им произвольные начальные значения. 
let a_3 = -2
let b_3 = -5

if (a_3 >= 0 && b_3 >= 0) {
    console.log(`FIRST:`, a_3 - b_3 )  // если a и b положительные, вывести их разность, Ноль можно считать положительным числом
} else if ( a_3 < 0 && b_3 < 0) {
    console.log(`SECOND:` ,a_3 * b_3) // если а и b отрицательные, вывести их произведение
}else {
    console.log(`THIRD:`,a_3 + b_3) // если а и b разных знаков, вывести их сумму
}

// 4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch
// организовать вывод чисел от a до 15

let a_4 = 16
switch (a_4) {
    case 0:
        console.log(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 1:
        console.log(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 2:
        console.log(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 3:
        console.log(3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 4:
        console.log(4, 5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 5:
        console.log(5, 6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 6:
        console.log(6, 7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 7:
        console.log(7, 8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 8:
        console.log(8, 9, 10, 11, 12 , 13 ,14, 15)
        break
    case 9:
        console.log(9, 10, 11, 12 , 13 ,14, 15)
        break        
    case 10:
        console.log(10, 11, 12 , 13 ,14, 15)
        break
    case 11:
        console.log(11, 12 , 13 ,14, 15)
        break        
    case 12:
        console.log(12 , 13 ,14, 15)
        break
    case 13:
        console.log(13 ,14, 15)
        break       
    case 14:
        console.log(14, 15)
        break       
    case 15:
        console.log(15)
        break      
    default:
        console.log('Error')
        break
}

// 5. Реализовать четыре основные арифметические операции в виде функций с двумя
// параметрами. Обязательно использовать оператор return.


function func_plus(a_5, b_5) {
    return a_5 + b_5
}

function func_minus(a_5, b_5) {
    return a_5 - b_5
}

function func_multiply(a_5, b_5) {
    return a_5 * b_5
}

function func_division(a_5, b_5) {
    switch (b_5) {
        case 0:
            console.log('Division by ZERO')  // не знаю насколько это верно, но попробовал исключить деление на 0.
            break
    default:
        return a_5 / b_5        
        break
    }
}

console.log(func_plus(10, 5))
console.log(func_minus(10,5))
console.log(func_multiply(10,5))    
console.log(func_division(10,5))

// 6. Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
// где arg1, arg2 — значения аргументов, operation — строка с названием операции. В
// зависимости от переданного значения выполнить одну из арифметических операций
// (использовать функции из пункта 5) и вернуть полученное значение (применить switch).

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case 'plus':
            return arg1 + arg2
            break
        case 'minus':
            return arg1 - arg2
            break
        case 'multiply':
            return arg1 * arg2
            break
        case 'division':
                switch (arg2) {
                    case 0:
                        console.log('Division by ZERO')  // не знаю насколько это верно, но попробовал исключить деление на 0.
                        break
                default:
                    return arg1 / arg2        
                    break
                }
        default:
            console.log('WRONG OPERATION')
            break
        
        }
        
    }


console.log(mathOperation(100,4,'division'))
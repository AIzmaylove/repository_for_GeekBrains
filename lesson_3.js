// 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

for (var counter = 0; counter <= 100; counter++) {
    if (counter !==0) { 
        if (counter <3){ console.log(counter)
        } else {
    var a = counter - 1
    while (counter % a !== 0){ 
        var a = a - 1 
        if (a === 1){
             console.log(counter); } 
            } 
        } 
    } 
}


// 2. Товары в корзине хранятся в массиве. Задачи:
// a. Организовать такой массив для хранения товаров в корзине;

let my_basket = [{name: 'iPhone 15', photo: 'dvsed.jpg', price: 2000}, {name: 'iPhone 13', photo: 'dffdad.jpg', price: 1000},
{name: 'iPhone 11', photo: 'xczvz.jpg', price: 700}, {name: 'iPhone 15 case', photo: 'vfbfga.jpg', price: 50},
{name: 'Tesla Phone', photo: 'ttdfv.jpg', price: 800}
]

// b. Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
let totalSum = 0 
for (var j = 0; j < my_basket.length; j++) {
    console.log('for array: ', my_basket[j].price)
    totalSum = totalSum + my_basket[j].price

}
console.log('Сумма стоимости корзины - ' , totalSum)


// 4. Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла.
for (var count = 0; count < 10; count++)
console.log(count)

// 5. Нарисовать пирамиду с 20 рядами с помощью console.log
let z = ' '
for (let p = 1; p <= 20; p++) {
    z = z + "*"
    console.log(z)
}
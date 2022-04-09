// 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999,
// надо получить на выходе объект, в котором в соответствующих свойствах описаны единицы,
// десятки и сотни. Например, для числа 245 надо получить следующий объект: {‘единицы’: 5,
// ‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо выдать соответствующее
// сообщение с помощью console.log и вернуть пустой объект


function myFunc (arg) {
    let n = arg 
    let number = String(n)
    let numberObject = {
            единицы: number[2],
            десятки: number[1],
            сотни: number[0] 
        
        }
    console.log(n)
    if (n > 999) {
        console.log('ОШИБКА!')
    } else if (n < 10) {
        numberObject.единицы = numberObject.сотни
        delete numberObject.сотни
        delete numberObject.десятки
        console.log(numberObject)
    } else if ( n > 10 && n < 100) {
        numberObject.единицы = numberObject.десятки
        numberObject.десятки = numberObject.сотни
        delete numberObject.сотни
        console.log(numberObject)
    } else {
        console.log(numberObject)
    }
}

console.log(myFunc(123))

// 2. Продолжить работу с интернет-магазином:
//     a. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими
//     объектами можно заменить их элементы?
//     b. Реализуйте такие объекты.
//     c. Перенести функционал подсчета корзины на объектно-ориентированную базу.


let my_basket_price = {
    getPrice () {
        return `${this.price}`
    }
}

let phone = {
    name: 'iPhone',
    model: '15',
    photo: 'dvsed.jpg', 
    color: 'white',
    price: 2000
}

let phone_1 = {
    name: 'iPhone',
    model: '13',
    photo: 'dffdad.jpg', 
    color: 'black',
    price: 1000
}

let phone_2 = {
    name: 'iPhone 11', 
    photo: 'xczvz.jpg', 
    color: 'blue',
    price: 700
}

let case_1 = {
    name: 'iPhone 15 case', 
    photo: 'vfbfga.jpg', 
    price: 50
}

let phone_3 = {
    name: 'Tesla Phone', 
    photo: 'ttdfv.jpg', 
    color: 'metallic',
    price: 800
}

let my_Basket_4 = []
my_Basket_4.push(phone, phone_1, phone_2, phone_3, case_1)
console.log(my_Basket_4)

phone.__proto__ = my_basket_price
phone_1.__proto__ = my_basket_price
phone_2.__proto__ = my_basket_price
case_1.__proto__ = my_basket_price
phone_3.__proto__ = my_basket_price
console.log(Number(phone_1.getPrice()) + Number(phone.getPrice()) + 
    Number(phone_2.getPrice()) + Number(case_1.getPrice()) + Number(phone_3.getPrice()))
 




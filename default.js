var i =1;
do {
    document.write('멋쟁이사자 : '+ i++ +"<br/>");
}while (i <= 10)

document.write('===============<br/>')

var j = 1;

while (j<=10){
    document.write('멋쟁이사자j : '+ j++ +"<br/>");
}

// var digit = parseInt(prompt('숫자 입력  : '));
//
// switch (digit){
//     case 0:
//         document.write('zero');
//         break;
//     case 1:
//         document.write("one");
//         break;
//     case 2:
//         document.write("two");
//         break;
//     case 3:
//         document.write("three");
//         break;
//     case 4:
//         document.write("four");
//         break;
//     case 5:
//         document.write("five");
//         break;
//     case 6:
//         document.write("six");
//         break;
//     case 7:
//         document.write("seven");
//         break;
//     case 8:
//         document.write("eight");
//         break;
//     case 9:
//         document.write("nine");
//         break;
// }


// var letter = prompt("Enter a letter : ");
//
// letter = letter.toLowerCase();
//
// if(letter == 'a' || letter == 'a'|| letter== 'i' || letter == 'o' || letter == 'u'){
//     console.log('Vowel');
// } else {
//     console.log('Consonant');
// }


// var num1 = parseInt(prompt('첫번째 숫자 입력 : '));
// var num2 = parseInt(prompt('두번쨰 숫자 입력 :'));
//
// if(num1 < num2){
//     console.log("큰 수는 : "+ num2);
// }
//
// if(num1 > num2){
//     console.log('큰 수는 : '+ num1);
// }
//
// if(num1 == num2){
//     console.log('같은수');
// }
//
// if(num1 > num2){
//     console.log('큰 수 num1 : '+ num1);
// } else if (num1 < num2){
//     console.log("큰 수 num2 : " + num2);
// } else if (num1 == num2){
//     console.log("같은 수");
// }

// var num1 = 20;
// var num2 = 10;
// var num3 = "10";
// var num4 = 20;
// var num5 = 15;
//
// console.log('일반 크기비교');
// console.log(num1 > num2, num1, ">", num2);
// console.log(num1 >= num2, num1, ">=", num2);
// console.log(num1 <= num2, num1, '<', num2);
// console.log(num1 <= num2, num1, '<=', num2);
//
// console.log('같은지 여부 확인')
// console.log(num1 == num4,num1, '==' ,num4 );
// console.log(num1 != num4, num1,'!=', num4);
//
// //등호 3개는 타입까지 비교
// console.log('===');
// console.log(num1 === num3, num1,'===', num3);
// console.log(num2 === num3, num2, '===', num3);
// console.log(num2 == num3, num2, '==', num3);
//
// console.log('num1>num2 && num1>num5',num1>num2 && num1>num5);
// console.log('num1>num2 || num1>num5',num1>num2 || num1>num5);

// var cels = parseFloat(prompt("섭씨 입력 : "));
// var farn = cels * (9/5)+32;
// document.write("화씨 : "+farn)

//
// var base = parseFloat(prompt("밑변 입력"));
// var height = parseFloat(prompt("높이 입력"));
//
// var area = number = base * height * 0.5;
//
// document.write("삼각형의 넓이 : " + area);
//
//



// var input1 = prompt("Enter first number");
// var num1 = parseInt((input1));
//
// var num2 = parseInt(prompt("Enter second number : "));
// var lineBreack = "<br/>";
//
// var result = num1 + num2;
// document.write("the sum is : " + result + lineBreack);
//
// var result = num1 - num2;
// document.write("the sub is : " + result + lineBreack);
//
// var result = num1 * num2;
// document.write("the multiplication is : " + result + lineBreack);
//
// var result = num1 / num2;
// document.write("the divsion is : " + result + lineBreack);
//
// var result = num1 % num2;
// document.write("the remainder is : " + result + lineBreack);
//
//


// var num ="20"
// num = num.toString();
// console.log(typeof  num);
//
// var number=20;
// console.log(typeof  number);
//
// number = number.toString();
// console.log(number, typeof  number);
//
// var x =2.56789
// console.log(x.toFixed(1),typeof x.toFixed(1));
// console.log(x.toFixed(2));
// //toFixed 까지 반올림
// console.log(x.toPrecision(1),typeof x.toPrecision(1));
// console.log(x.toPrecision(2));
// //toPrecison 에서 반올림
// console.log(Number(true));
// console.log(Number(false));
// console.log(Number(" 10"));
// console.log(Number(" 10 "));
// console.log(Number("10.25"));
// //Number 숫자 변환해주는듯!



// var text = prompt("Enter your name");
// document.write("your name : "+text+"<br/>");
//
// var len =text.length;
// document.write("Number of characters : "+len +"<br/>")
//
// document.write(text.charAt(5)+"<br/>");
//
// document.write(text.toUpperCase()+"<br/>");
// document.write(text.toLowerCase()+"<br/>");
//
//
// var text1 = 'hi';
// var text2 = "bye";
// var text3 = text1.concat(text2);
// var text4 = text1 + text2;
// document.write(text3+"<br/>");
// document.write(text4+"<br/>");
// //concat 문자열 붙이는 함수인듯
//
// var text4 = "hello";
// var result = text4.slice(1,2)
// document.write(result+"<br/>");


// var lName = '홍'
// var fName ='길동';
//
// var fullName =lName+fName;
//
// console.log(fullName);
// console.log("Today is"+ " a "+ "beaultful day");
// console.log("My name is "+ fullName);
//
// var num1 =20;
// var num2 = 30;
// var sum = num1+num2;
// console.log(num1+" + "+num2+" = "+sum);
// console.log(""+num1+num2);
// console.log(num1+num2);



// var name = "이승훈";
// var age =29;
// var cgpa =3.92;
// var lineBreak = "<br/>";
//
// document.write("이름: " + name + lineBreak);
// document.write("나이: " + age + lineBreak);
// document.write("학점: " + cgpa + lineBreak);
//


// console.log(typeof 123);
// console.log(typeof  123.5);
// console.log(typeof "123");
// console.log(typeof  true);
// console.log(typeof false);

// var car;
// console.log(typeof car);
// var car =" ";
// console.log(typeof car);
// var person ={firstName: "John",lastNaMe:"Doe",age:50,eyeColor:"blue"};
// console.log(typeof person);
//

// document.write("Hello World");
// document.write("<h1>Welcom to JS Program</h1>");
// document.write("<h2>Welcome to Js Program</h2>");
//
// console.log('Welcome to Js Program');
// console.info('Welcome to Js Program');
// console.warn('Welcome to Js Program');
// console.error('Welcome to Js Program');
//
// alert('Welcome JS Program');
// var a = prompt('Welcome to Js Program');
// console.log(a);
//  ++는 과거연산기록이있어야해서 못쓴다?
// 동시실행으로 최적화가 많아졌는데 ++은 순차실행이라 속도에 문제가있다?

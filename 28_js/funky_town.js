//Cheryl Qian
//SoftDev1 pd8
//K28 -- Sequential Progression
//2018-12-18

var fibonacci = (num) => {
    if (num == 0) {
	return 0;
    }
    else if (num == 1) {
	return 1;
    }
    
    else {
	return fibonacci(num -  1) + fibonacci(num - 2);
    }
}


var gcd = (a,b) => {
    if ( b == 0 ) {
	return a;
    }
    return gcd(b,a%b);
}

var randomStudent = () => {
    var num = Math.floor(Math.random() * list.length);
    return list[num]
}

var list = ["cheryl","lois","alex","fahim","deedee","erica"];

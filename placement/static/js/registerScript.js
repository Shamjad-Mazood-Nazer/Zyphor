
	function admnoValidation(inputTxt){

		var regx = /^[0-9]{4,}$/;
		var textField = document.getElementById("admno");

		if(inputTxt.value != '' ){
			if(inputTxt.value.match(regx)){
				textField.textContent = '';
				textField.style.color = "green";
			}else{
				textField.textContent = '* not a valid number!!!';
				textField.style.color = "red";
			}
		}
//		else if(inputTxt.value.length() != 5){
//			textField.textContent = '* not a valid number!!!';
//			textField.style.color = "red";
//		}
		else{
			textField.textContent = '* your input is empty';
			textField.style.color = "red";
		}
	}

function fnameValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("fname");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 2){

            if(inputTxt.value.match(regx)){
                textField.textContent = '';
                textField.style.color = "green";

            }else{
                textField.textContent = 'only characters allowded';
                textField.style.color = "red";
            }
        }else{
            textField.textContent = 'your input must be more than two chracters';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function lnameValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("lname");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 2){

            if(inputTxt.value.match(regx)){
                textField.textContent = '';
                textField.style.color = "green";

            }else{
                textField.textContent = 'only characters allowded';
                textField.style.color = "red";
            }
        }else{
            textField.textContent = 'your input must be more than two chracters';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}


	function emailValidation(inputTxt){
		// ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
		var regx = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
		var textField = document.getElementById("email");

		if(inputTxt.value != '' ){
			if(inputTxt.value.match(regx)){
				textField.textContent = '';
				textField.style.color = "green";
			}else{
				textField.textContent = '* email is not valid!!!';
				textField.style.color = "red";
			}
		}else{
			textField.textContent = '* your input is empty';
			textField.style.color = "red";
		}
	}


	function passwordValidation(inputTxt){

		var regx = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,}/;
		var textField = document.getElementById("pass1");

		if(inputTxt.value != '' ){
			if(inputTxt.value.match(regx)){
				textField.textContent = '';
				textField.style.color = "green";

			}else{
				textField.textContent = '* Must contain at least one number and one uppercase and lowercase letter and aleast 5 characters';
				textField.style.color = "red";
			}
		}else{
			textField.textContent = '* your input is empty';
			textField.style.color = "red";
		}
	}


    function cpasswordValidation(inputTxt){

        var regx =  document.getElementById("pass").value;
        var regy =  document.getElementById("repass").value;
        var textField = document.getElementById("pass2");
        var textField1 = document.getElementById("pass1");

        if(inputTxt.value != '' ){
            if(regx == regy){
                textField.textContent = '';
                textField.style.color = "green";

            }else{
                textField.textContent = '* not match';
                textField.style.color = "red";
            }
        }else{
            textField.textContent = '* missing';
            textField.style.color = "red";
        }
    }


	function emailValidation(inputTxt){
		// ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
		var regx = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
		var textField = document.getElementById("mail");

		if(inputTxt.value != '' ){
			if(inputTxt.value.match(regx)){
				textField.textContent = '';
				textField.style.color = "green";
			}else{
				textField.textContent = 'email is not valid!!!';
				textField.style.color = "red";
			}
		}else{
			textField.textContent = 'your input is empty';
			textField.style.color = "red";
		}
	}


	function passwordValidation(inputTxt){

		var regx = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}/;
		var textField = document.getElementById("pass");

		if(inputTxt.value != '' ){
			if(inputTxt.value.match(regx)){
				textField.textContent = '';
				textField.style.color = "green";

			}else{
				textField.textContent = 'Must contain at least one number and one uppercase and lowercase letter and aleast 6 characters';
				textField.style.color = "red";
			}
		}else{
			textField.textContent = 'your input is empty';
			textField.style.color = "red";
		}
	}

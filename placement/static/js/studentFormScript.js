function inputValidation(inputTxt){

    var regx = /^[0-9a-zA-Z ]+$/;
    var textField = document.getElementById("textField");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 5){

            if(inputTxt.value.match(regx)){
                textField.textContent = 'Good input';
                textField.style.color = "green";

            }else{
                textField.textContent = 'only numbers, letters And White space';
                textField.style.color = "red";
            }
        }else{
            textField.textContent = 'your input is less than 5 chracters';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function nameValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("name");

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

function fatherNameValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("father_name");

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

function motherNameValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("mother_name");

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

function addressValidation(inputTxt){

    var regx = /^[a-zA-Z-()]+$/;
    var textField = document.getElementById("addr");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 4){

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
        textField.textContent = 'your email input is empty';
        textField.style.color = "red";
    }
}

function fatherPhoneValidation(inputTxt){

    var regx = /^[6-9][0-9]{10}$/;
    var textField = document.getElementById("fatherph");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";
            }else{
                textField.textContent = '**not valid phone number';
                textField.style.color = "red";
            }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function phone1Validation(inputTxt){

    var regx = /^[6-9][0-9]{10}$/;
    var textField = document.getElementById("ph1");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";
            }else{
                textField.textContent = '**not valid phone number';
                textField.style.color = "red";
            }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function phone2Validation(inputTxt){

    var regx = /^[6-9][0-9]{10}$/;
    var textField = document.getElementById("ph2");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";
            }else{
                textField.textContent = '**not valid phone number';
                textField.style.color = "red";
            }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function sslcPerValidation(inputTxt){

    var regx = /\b(?<!\.)(?!0+(?:\.0+)?%)(?:\d|[1-9]\d|100)(?:(?<!100)\.\d+)?%;
    var textField = document.getElementById("sslcper");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";
            }else{
                textField.textContent = '**not valid %';
                textField.style.color = "red";
            }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function motherPhoneValidation(inputTxt){

    var regx = /^[6-9][0-9]{10}$/;
    var textField = document.getElementById("motherph");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";
            }else{
                textField.textContent = '**not valid phone number';
                textField.style.color = "red";
            }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}


function cityValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("cit");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 1){

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

function districtValidation(inputTxt){

    var regx = /^[a-zA-Z]+$/;
    var textField = document.getElementById("states");

    if(inputTxt.value != '' ){

        if(inputTxt.value.length >= 1){

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

function pincodeValidation(inputTxt){

    var regx = /^[6][0-9]{5}$/;
    var textField = document.getElementById("pin");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";

        }else{
            textField.textContent = 'only valid pincode';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function cgpaValidation(inputTxt){

    var regx = /^[0-9]\.\d{1}$/;
    var textField = document.getElementById("cgpa");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";

        }else{
            textField.textContent = 'only valid cgpa';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function dobValidation(inputTxt){

    var regx = /s+(?:0[1-9]|[12][0-9]|3[01])[-/.](?:0[1-9]|1[012])[-/.](?:19\d{2}|20[01][0-9]|2002)\b/;
    var textField = document.getElementById("birth");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";

        }else{
            textField.textContent = 'only valid year';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}

function universityNoValidation(inputTxt){

    var regx = /AJC\d\d+[A-Z]+-\d\d\d\d/;
    var textField = document.getElementById("universityno");

    if(inputTxt.value != '' ){
        if(inputTxt.value.match(regx)){
            textField.textContent = '';
            textField.style.color = "green";

        }else{
            textField.textContent = 'only valid number';
            textField.style.color = "red";
        }
    }else{
        textField.textContent = 'your input is empty';
        textField.style.color = "red";
    }
}


//<!--<script>-->
//<!--    $(document).ready(function() {-->
//<!--        $('#contact_form').bootstrapValidator({-->
//<!--            // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later-->
//<!--            feedbackIcons: {-->
//<!--                valid: 'glyphicon glyphicon-ok',-->
//<!--                invalid: 'glyphicon glyphicon-remove',-->
//<!--                validating: 'glyphicon glyphicon-refresh'-->
//<!--            },-->
//<!--            fields: {-->
//<!--                first_name: {-->
//<!--                    validators: {-->
//<!--                        stringLength: {-->
//<!--                            min: 2,-->
//<!--                        },-->
//<!--                        notEmpty: {-->
//<!--                            message: 'Please supply your first name'-->
//<!--                        }-->
//<!--                    }-->
//<!--                },-->
//<!--                last_name: {-->
//<!--                    validators: {-->
//<!--                        stringLength: {-->
//<!--                            min: 2,-->
//<!--                        },-->
//<!--                        notEmpty: {-->
//<!--                            message: 'Please supply your last name'-->
//<!--                        }-->
//<!--                    }-->
//<!--                },-->
//<!--                email: {-->
//<!--                    validators: {-->
//<!--                        notEmpty: {-->
//<!--                            message: 'Please supply your email address'-->
//<!--                        },-->
//<!--                        emailAddress: {-->
//<!--                            message: 'Please supply a valid email address'-->
//<!--                        }-->
//<!--                    }-->
//<!--                },-->
//<!--                phone: {-->
//<!--                    validators: {-->
//<!--                        notEmpty: {-->
//<!--                            message: 'Please supply your phone number'-->
//<!--                        },-->
//<!--                        phone: {-->
//<!--                            country: 'US',-->
//<!--                                message: 'Please supply a vaild phone number with area code'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    },-->
//<!--                    address: {-->
//<!--                        validators: {-->
//<!--                            stringLength: {-->
//<!--                                min: 8,-->
//<!--                            },-->
//<!--                            notEmpty: {-->
//<!--                                message: 'Please supply your street address'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    },-->
//<!--                    city: {-->
//<!--                        validators: {-->
//<!--                            stringLength: {-->
//<!--                                min: 4,-->
//<!--                            },-->
//<!--                            notEmpty: {-->
//<!--                                message: 'Please supply your city'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    },-->
//<!--                    state: {-->
//<!--                        validators: {-->
//<!--                            notEmpty: {-->
//<!--                                message: 'Please select your state'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    },-->
//<!--                    zip: {-->
//<!--                        validators: {-->
//<!--                            notEmpty: {-->
//<!--                                message: 'Please supply your zip code'-->
//<!--                            },-->
//<!--                            zipCode: {-->
//<!--                                country: 'US',-->
//<!--                                message: 'Please supply a vaild zip code'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    },-->
//<!--                    comment: {-->
//<!--                        validators: {-->
//<!--                            stringLength: {-->
//<!--                                min: 10,-->
//<!--                                max: 200,-->
//<!--                                message:'Please enter at least 10 characters and no more than 200'-->
//<!--                            },-->
//<!--                            notEmpty: {-->
//<!--                                message: 'Please supply a description of your project'-->
//<!--                            }-->
//<!--                        }-->
//<!--                    }-->
//<!--                }-->
//<!--            })-->
//<!--            .on('success.form.bv', function(e) {-->
//<!--                $('<div id="suc"></div>cess_message').slideDown({ opacity: "show" }, "slow") // Do something ...-->
//<!--                $('#contact_form').data('bootstrapValidator').resetForm();-->
//
//<!--                // Prevent form submission-->
//<!--                e.preventDefault();-->
//
//<!--                // Get the form instance-->
//<!--                var $form = $(e.target);-->
//
//<!--                // Get the BotstrapValidator instance-->
//<!--                var bv = $form.data('bootstrapValidator');-->
//
//<!--                // Use Ajax to submit form data-->
//<!--                $.post($form.attr('action'), $form.serialize(), function(result) {-->
//<!--                    console.log(result);-->
//<!--            }, 'json');-->
//<!--        });-->
//<!--    });-->
//<!--</script>-->

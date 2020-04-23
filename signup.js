//Project 01   Created: 4/16/2020     Due: 4/22/2020   signup.js
//Created By Paul Schartung & Modified By Andre Hichue & Megan Reardon
//This file consists of the functions used in signup.html which sets parameters for password requirements, username, and ensure all requirements are filled out before creating an account on our website

// This function uses REGEX to make sure all components of the form is filled out before submission
//Modified By Andre Hichue-Created This Function
function check_all(){ // attempt to call all the functions before submission

  var nameCheck = document.forms["signup_form"]["name"];
  var passwordCheck = document.forms["signup_form"]["pwd"];
  var userNameCheck = document.forms["signup_form"]["usrname"];
  var password2Check = document.forms["signup_form"]["pwd2"];
  var passReq = /\w{6,}[0-9]{1,}/;
  var pwdError=document.getElementById("pwdError");
  var pwd2Error=document.getElementById("pwd2Error");
  var pwd_val = document.getElementById("pwd").value;
  var pwd2_val = document.getElementById("pwd2").value;
  // var name_val=document.getElementById("name").value;
  var test = new RegExp(/\w{6,}[0-9]{1,}/);


  if (nameCheck.value == "") {
    nameCheck.focus();
    // This will focus the mouse back on the input box
    return false;
  }
  // if(test != true) {
  //   passwordCheck.focus();
  //   pwdError.style.color = "red";
  //   pwdError.innerHTML = "*Your password must be at least 6 characters and 1 number";
  //   return false;
  // }
  if (pwd_val != pwd2_val){
    pwd2Error.style.color = "red";
    pwdError.style.color = "red";
    pwd2Error.innerHTML = "*Your passwords must match!";
    passwordCheck.focus();
    password2Check.focus();
    return false;
  }
  if (userNameCheck.value == "") {
    userNameCheck.focus();
    // This will focus the mouse back on the input box
    return false;
  }

  if(passwordCheck.value.match(passReq)) {
  }
  else {
    passwordCheck.focus();
    pwdError.innerHTML = "*Your password must be at least 6 characters and 1 number.";
    return false;
  }

  return true;
}

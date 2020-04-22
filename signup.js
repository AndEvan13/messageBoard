//Project 01   Created: 4/16/2020     Due: 4/22/2020   signup.js
//Created By Paul Schartung & Modified By Andre Hichue & Megan Reardon
//This file consists of the functions used in signup.html which sets parameters for password requirements, username, and ensure all requirements are filled out before creating an account on our website

// This function uses REGEX to make sure a name is entered
//Modified by Megan Reardon For XSS
function check_name(){//Checks Name
   var name_val=document.getElementById("name").value;
   var nameError=document.getElementById("nameError");
   var name_val=str.replace(/</gi, "&lt"); //Prevents Cross-Site Scripting
   if (name_val==""){//if the field is empty:
      nameError.style.color = "red";
      nameError.innerHTML=  "*Please enter a name";
      return false;
   }
   else{
   nameError.innerHTML = "";
   return true;
   }
}
// This function uses REGEX to make sure a usrname is entered and is checked to make sure there are no users with the same username
//Modified by Megan Reardon For XSS
function check_usrname(){ //checks username input
  var usrname_val=document.getElementById("usrname").value;
  var usrnameError=document.getElementById("usrnameError");
  var usrname_val = str.replace(/</gi, "&lt"); // Prevents Cross-Site Scriptng
  if (usrname_val==""){ //if the field is empty:
    usrnameError.style.color = "red";
    usrnameError.innerHTML = "*Please enter a username";
    return false;
  }
  else{
    usrnameError.innerHTML = "";
    return true;
  }
}
////////////////////////////////////////////////////////////////////////
// This function uses REGEX to make sure the password is within the described parameters - at least 6 characters and one number
//Modified by Megan Reardon For XSS
function check_pwd(){ //validates password input
  var pwd_pattern = new RegExp(/\w{6,}[0-9]{1,}/);
  var pwd_val = document.getElementById("pwd").value;
  var pwd2_val = document.getElementById("pwd2").value;
  var test = pwd_pattern.test(pwd_val);
  var pwdError=document.getElementById("pwdError");
  var pwd2Error=document.getElementById("pwd2Error");
  var pwd_val = str.replace(/</gi. "&lt"); //Prevents Cross-Site Scripting
  var pwd2_val = str.replace(/</gi. "&lt"); //Prevents Cross-Site Scripting
  // document.write(test)
  if (test == false){ //if it does not match the regex:
    pwdError.style.color = "red";
    pwdError.innerHTML = "*Your password must be at least six characters and one number";
    return false;
  }
  if (pwd_val != pwd2_val){
    pwd2Error.style.color = "red";
    pwd2Error.innerHTML = "*Your password must match";
  }
  else{
    pwdError.innerHTML = "";
    pwd2Error.innerHTML = "";
    return true;
   }
 }

// This function uses REGEX to make sure all components of the form is filled out before submission
//Modified By Andre Hichue-Created This Function
 function check_all(){ // attempt to call all the functions before submission
  // var t4 = replace_bads();
  var t1 = check_name();
  var t2 = check_usrname();
  var t3 = check_pwd();
  // console.log((t1 & t2 & t3))
  if ((t1 || t2 || t3) != true ){
    alert("Please double check your inputs")
    return false;
  }
  else{
    return true
  }
}
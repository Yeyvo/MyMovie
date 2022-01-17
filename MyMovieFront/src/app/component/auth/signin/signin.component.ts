import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";
import {AbstractControl, FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import { faGoogle } from '@fortawesome/free-brands-svg-icons';
import {TooltipPosition} from "@angular/material/tooltip";

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.scss']
})
export class SigninComponent implements OnInit {

  signInForm: FormGroup;
  errorMessage: String;
  faGoogle = faGoogle;

  constructor(public auth: AuthService, private router: Router, private formBuilder: FormBuilder) {
  }

  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this. signInForm = this.formBuilder.group({
      email: ['',[ Validators.required, Validators.email] ],
      password: ['',[ Validators.required]]
    });
  }


  onConnect(){
    const email = this.signInForm.get('email').value;
    const password = this.signInForm.get('password').value;
    this.auth.signInUser(email,password).then(()=>{
      console.log('Successfully connected !');
      this.router.navigate(['/']);
    }).catch((err)=>{
      console.log(err);
      this.errorMessage = err;
    });
  }

  resetPassWordEmail() {
    const email = this.signInForm.get('email');
    if(email.value !== "" && email.status === "VALID"){
      this.errorMessage = " An Email has been sent to the specified Email address"
      this.auth.sendResetEmail(email.value);
    }
    if(email.status !== "VALID") {
      this.checkValidityForError(false);
    }

  }
  checkValidityForError(invalid: boolean) {
    if (invalid) {
      this.errorMessage = "Invalid Form check all Inputs"
    } else{
      this.errorMessage = ""
    }
  }
}

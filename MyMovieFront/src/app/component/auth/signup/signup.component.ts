import {Component, OnInit} from '@angular/core';
import {AbstractControl, FormBuilder, FormGroup, ValidationErrors, ValidatorFn, Validators} from "@angular/forms";
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";
import { faGoogle } from '@fortawesome/free-brands-svg-icons';
import {TooltipPosition} from "@angular/material/tooltip";

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  signUpForm: FormGroup;
  errorMessage: string;
  faGoogle = faGoogle;
  positionOption: TooltipPosition= 'above';


  constructor(
    public auth : AuthService,
    private formBuilder: FormBuilder,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this.signUpForm = this.formBuilder.group(
      {
        username: ['', [Validators.required]],
        email: ['', [Validators.email, Validators.required]],
        password: ['', [Validators.required, Validators.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\w\W]{8,}$/)]],
        confirmPassword: ['',  {Validators: this.checkPasswords}]
      }
    );
  }

  onSaveAccount() {
    const username = this.signUpForm.get('username').value;
    const email = this.signUpForm.get('email').value;
    const password = this.signUpForm.get('password').value;
    this.auth.createNewUserEmailPass(username, email, password).then(() => {
      this.router.navigate(['/']);
    }).catch((err) => {
      this.errorMessage = err;
      console.log(err);
    });
  }

  checkValidityForError(invalid: boolean) {
    if (invalid) {
      this.errorMessage = "Invalid Form check all Inputs"
    } else{
      this.errorMessage = ""
    }
  }

  checkPasswords: ValidatorFn = (group: AbstractControl):  ValidationErrors | null => {
    let pass = group.get('password').value;
    let confirmPass = group.get('confirmPassword').value
    return pass === confirmPass ? null : { notSame: true }
  }
}

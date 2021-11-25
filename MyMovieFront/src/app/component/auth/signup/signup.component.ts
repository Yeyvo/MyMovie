import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";
import { faGoogle } from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  signUpForm: FormGroup;
  errorMessage: string;
  faGoogle = faGoogle;


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
        password: ['', [Validators.required, Validators.pattern(/[A-Za-z0-9]{6,}/)]]
      }
    );
  }

  onSaveAccount() {
    const username = this.signUpForm.get('username').value;
    const email = this.signUpForm.get('email').value;
    const password = this.signUpForm.get('password').value;
    this.auth.createNewUserEmailPass(username, email, password).then(() => {
      this.router.navigate(['/books']);
    }).catch((err) => {
      this.errorMessage = err;
      console.log(err);
    });
  }
}

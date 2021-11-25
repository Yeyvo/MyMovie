import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import { faGoogle } from '@fortawesome/free-brands-svg-icons';

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
      password: ['',[ Validators.required, Validators.pattern(/[0-9a-zA-Z]{6,}/)]]
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
}

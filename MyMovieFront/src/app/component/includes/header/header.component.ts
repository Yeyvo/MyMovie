import {Component, OnDestroy, OnInit} from '@angular/core';
import {faBars, faSearch, faTimes} from '@fortawesome/free-solid-svg-icons';
import {AuthService} from "../../../services/auth.service";
import {User} from "../../../models/User";
import {Observable, Subscription} from "rxjs";
import {MoviesService} from "../../../services/movies.service";
import {MoviesComponent} from "../../movies/movies.component";
import {Router} from "@angular/router";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit, OnDestroy {

  isMenuCollapsed: boolean = true;
  itemsActive: boolean = false;
  menuBtnHide: boolean = false;
  searchBtnHide: boolean = false;
  cancelBtnShow: boolean = false;
  formActive: boolean = false;
  faSearch = faSearch;
  faTimes = faTimes;
  faBars = faBars;
  profileActive: boolean = false;

  isAuth: boolean;
  authSubscription: Subscription;
  user: User;
  userSub : Subscription;
  searchRes: any;
  searchStr: string;


  constructor(
    public auth: AuthService,
    private movieService : MoviesService,
    private router : Router
  ) {
  }

  ngOnInit(): void {
    // this.isAuth = this.auth.isAuth;
    this.authSubscription = this.auth.authSubject.subscribe((newData) => {
      this.isAuth = newData;
    });

    this.userSub = this.auth.user$.subscribe((newUser)=>{
      this.user = newUser;
    });

  }

  onSignOUt() {
    this.auth.signOut();
  }

  onClickMenuBtn() {

    this.itemsActive = true
    this.menuBtnHide = true;
    this.searchBtnHide = true;
    this.cancelBtnShow = true;
    this.profileActive = false;

    this.formActive = false;
    this.searchBtnHide = false;
  }

  onClickCancelBtn() {
    this.itemsActive = false
    this.menuBtnHide = false;
    this.searchBtnHide = false;
    this.cancelBtnShow = false;
    this.formActive = false;
    this.profileActive = false;
  }

  onClickSearchBtn() {
    this.onClickCancelBtn();

    this.formActive = true;
    this.searchBtnHide = true;
    this.cancelBtnShow = true;

  }

  onClickItem() {
    this.onClickCancelBtn();
  }

  onClickItemProfile() {
    this.profileActive = false;
  }

  ngOnDestroy(): void {
    this.authSubscription.unsubscribe();
    this.userSub.unsubscribe();
  }

  searchMovies() {
    this.movieService.searchMovies(this.searchStr, 1);
    this.router.navigate(['/movies']);
  }

  onLogo() {
    this.onClickCancelBtn();
    this.router.navigate(['/']);
  }
}

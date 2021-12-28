import {Component, OnDestroy, OnInit} from '@angular/core';
import {faBars, faSearch, faTimes} from '@fortawesome/free-solid-svg-icons';
import {AuthService} from "../../../services/auth.service";
import {User} from "../../../models/User";
import {Observable, Subscription} from "rxjs";
import {MoviesService} from "../../../services/movies.service";
import {MoviesComponent} from "../../movies/movies.component";
import {Router} from "@angular/router";
import {delay} from "rxjs/internal/operators/delay";

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

  hidenNav: boolean = false;

  faSearch = faSearch;
  faTimes = faTimes;
  faBars = faBars;
  profileActive: boolean = false;

  isAuth: boolean;
  authSubscription: Subscription;
  user: User;
  userSub: Subscription;
  searchRes: any;
  searchStr: string;


  constructor(
    public auth: AuthService,
    private movieService: MoviesService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    // this.isAuth = this.auth.isAuth;
    this.authSubscription = this.auth.authSubject.subscribe((newData) => {
      this.isAuth = newData;
    });

    this.userSub = this.auth.user$.subscribe((newUser) => {
      this.user = newUser;
    });

    var prevScrollpos = window.pageYOffset;
    window.onscroll = function() {
      var currentScrollPos = window.pageYOffset;
      if (prevScrollpos > currentScrollPos) {
          this.hidenNav = false;
      } else {
        this.hidenNav = true;
      }
      prevScrollpos = currentScrollPos;
    }

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
    this.disableScrolling();

    this.formActive = false;
    this.searchBtnHide = false;
  }

  onClickCancelBtnMenu() {
    this.itemsActive = false
    this.menuBtnHide = false;
    this.searchBtnHide = false;
    this.cancelBtnShow = false;
    this.formActive = false;

  }

  onClickCancelBtn() {
    this.onClickCancelBtnMenu();
    this.profileActive = false;

    this.enableScrolling();
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
    if (this.searchStr !== undefined /*|| this.searchStr !== ''*/) {
      this.movieService.searchMovies(this.searchStr, 1);
      this.searchStr = '';
      this.router.navigate(['/movies']);
    } else {
      this.getMoviesBtnClick();
    }
  }

  getMoviesBtnClick(){
    this.getTopRatedMovies(1);
    this.router.navigate(['/movies']).then(() => {
      window.location.reload();
    });
  }


  getTopRatedMovies(page: number) {
    this.movieService.getTopRatedMovies(page).pipe(delay(2000)).subscribe((res: any) => {
        this.searchRes = res.total_results;
      },
      error => console.log(error));
  }

  onLogo() {
    this.onClickCancelBtn();
    this.router.navigate(['/']);
  }

  disableScrolling() {
    // var x = window.scrollX;
    // var y = window.scrollY;
    // window.onscroll = function () {
    //   window.scrollTo(x, y);
    // };
  }

  enableScrolling() {
    // window.onscroll = function () {
    // };
  }
}

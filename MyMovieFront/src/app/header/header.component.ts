import {Component, OnInit} from '@angular/core';
import {faBars, faSearch, faTimes} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  isMenuCollapsed: boolean = true;
  isAuth: boolean = true;
  itemsActive: boolean = false;
  menuBtnHide: boolean = false;
  searchBtnHide: boolean = false;
  cancelBtnShow: boolean = false;
  formActive: boolean = false;
  faSearch = faSearch;
  faTimes = faTimes;
  faBars = faBars;
  profileActive :boolean = false;

  constructor() {
  }

  ngOnInit(): void {
  }

  onSignOUt() {

  }

  onClickMenuBtn() {

    this.itemsActive = true
    this.menuBtnHide = true;
    this.searchBtnHide = true;
    this.cancelBtnShow = true;
  }

  onClickCancelBtn() {
    this.itemsActive = false
    this.menuBtnHide = false;
    this.searchBtnHide = false;
    this.cancelBtnShow = false;
    this.formActive = false;
  }

  onClickSearchBtn() {
    this.formActive = true;
    this.searchBtnHide = true;
    this.cancelBtnShow = true;

  }

  onClickItem() {
    this.onClickCancelBtn();
  }
  // onClickProfile(){
  //   this.profileActive = true;
  // }
  onClickItemProfile(){
    this.profileActive = false;
  }
}

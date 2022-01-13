import {Component, OnInit} from '@angular/core';
import {MovieRecommendationService} from "../../services/MovieRecommendation.service";

@Component({
  selector: 'app-recommendation',
  templateUrl: './recommendation.component.html',
  styleUrls: ['./recommendation.component.scss']
})
export class RecommendationComponent implements OnInit {

  recommendationTree: any ;
  isResult: boolean = false;
  recomendMovies: any;
  responsiveOptions = [
    {
      breakpoint: '1024px',
      numVisible: 3,
      numScroll: 3
    },
    {
      breakpoint: '768px',
      numVisible: 2,
      numScroll: 2
    },
    {
      breakpoint: '560px',
      numVisible: 1,
      numScroll: 1
    }
  ];

  constructor(public RecommendationEngine: MovieRecommendationService) {

  }

  ngOnInit(): void {
    this.RecommendationEngine.getRecomendation().subscribe((res) => {
      this.recommendationTree = res;
    });
  }


  clickTrue() {
    this.recommendationTree = this.recommendationTree.TrueChild;
  }

  clickFalse() {
    this.recommendationTree = this.recommendationTree.FalseChild;
  }
}

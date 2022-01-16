import {Component, OnInit} from '@angular/core';
import {MovieRecommendationService} from "../../services/MovieRecommendation.service";
import {MoviesService} from "../../services/movies.service";

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
  loader:boolean=true;

  constructor(public RecommendationEngine: MovieRecommendationService, public movies:MoviesService) {

  }

  ngOnInit(): void {
    this.RecommendationEngine.getRecomendation().subscribe((res) => {
      this.recommendationTree = res;
      this.loader = false;
    });
  }


  clickTrue() {
    this.recommendationTree = this.recommendationTree.true_branch;

    this.found();
  }

  clickFalse() {
    this.recommendationTree = this.recommendationTree.false_branch;
    this.found();
    console.log(this.recommendationTree.recommendation)
  }

  found(){
    if(this.recommendationTree.recommendation !== undefined){
      this.movies.getMovie(this.recommendationTree.recommendation).subscribe((res)=>{
        this.recomendMovies = res;
        this.isResult = true;
      })

    }
  }
}

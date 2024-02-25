import { Component } from '@angular/core';

import {categories, Category} from '../categories';
import { products } from '../products';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent {
  categories = [...categories];

  active: Category = {
    category: ""
  };

  addFilter(category:Category){
    this.active = category;

    products.forEach(el => {
      if(el.category === category.category && !el.removable){
        el.active = !el.active;
      } else{
        el.active = false;
      }
    })
  }
}

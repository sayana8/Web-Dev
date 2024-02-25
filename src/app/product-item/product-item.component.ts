import { Component, Input } from '@angular/core';
import { Product } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product: any
  isClicked = false;

  clickLike(product: Product){
    if(!this.isClicked){
      product.likes += 1;
    } 
    this.isClicked = true;
  }

  share(url: string) {
    var sharelink = "https://t.me/share/url?url="+url+"&text=Let me buy this! ";
    window.open(sharelink);
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

  removeItem(product: Product){
    product.removable = true;
    product.active = !product.active;
  }
}

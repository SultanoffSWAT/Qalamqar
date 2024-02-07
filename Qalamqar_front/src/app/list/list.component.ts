import { Component, OnInit} from '@angular/core';
import { Product } from "../product";
import { ServiceService } from "../../service/service.service";
import {ActivatedRoute} from "@angular/router";


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})

export class ListComponent implements OnInit{
  products: Product[] = [];
  test: Product[] = [];
  size = 0
  constructor(private service: ServiceService, private route: ActivatedRoute) {
    this.getList()
    this.sizeList()
  }
  getList() {
    this.service.getList().subscribe((data) => {
      // console.log(this.products = data)
      this.products = data
    })
  }

  sizeList() {
    this.service.getList().subscribe((data) => {
      this.size = data.length
    })
  }

  ngOnInit(): void {
    console.log(this.size)
  }

}

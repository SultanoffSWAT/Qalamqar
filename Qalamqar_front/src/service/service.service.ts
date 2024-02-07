import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Product} from "../app/product";

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http: HttpClient) {}
  getList(): Observable<Product[]>{
    return this.http.get<Product[]>('http://127.0.0.1:8000/api/products/')
  }

}

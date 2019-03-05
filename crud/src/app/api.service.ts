import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000"
  httpHeaders= new HttpHeaders({'Content-Type': 'application/json'})

  constructor(private http: HttpClient) { };

  getAllPosts(): Observable<any>{
    return this.http.get(this.baseurl + '/blog/?format=json',
      {headers: this.httpHeaders})
  }
  getOnePost(id): Observable<any>{
    return this.http.get(this.baseurl + '/blog/' + id + '/?format=json',
      {headers: this.httpHeaders})
  }
  updatePost(post): Observable<any>{
    const body = {title: post.title , content: post.content, date_posted: post.date_posted};
    return this.http.get(this.baseurl + '/blog/' + post.id + body + '/?format=json',
      {headers: this.httpHeaders})
  }
}


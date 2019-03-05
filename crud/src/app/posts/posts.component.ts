import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service'

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css'],
})

export class PostsComponent implements OnInit {
  posts = [{title: 'test'}];
  selectedPost;

  constructor(private  api: ApiService) {
    this.getPosts();
    this.selectedPost = {id: -1, title: '', content: '', date_posted: 0};

  }

  getPosts = () => {
    this.api.getAllPosts().subscribe(
      data => {
        this.posts = data;
      },
      error => {
        console.log(error);
      }
    );

  }

  postClicked = (post) => {
    this.api.getOnePost(post.id).subscribe(
      data => {
        this.selectedPost = data;
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );

  }
    updatePost = () => {
      this.api.updatePost(this.selectedPost).subscribe(
        data => {
          this.selectedPost = data;
          console.log(data);
        },
        error => {
          console.log(error);
        }
      );

    }

  ngOnInit() {
  }

}



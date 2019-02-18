import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { User} from "../user.model";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  users: User;

  constructor(private data: DataService) { }

  ngOnInit() {
    this.data.getUsers().subscribe(data => {
        this.users = data['users']
        console.log(this.users);
      }
    );
  }
}

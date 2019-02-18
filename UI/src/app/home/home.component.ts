import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { User} from "../user.model";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  users: User;

  constructor(private user: UserService) { }

  ngOnInit() {
    this.user.getAll().subscribe(data => {
        this.users = data['users']
        console.log(this.users);
      }
    );
  }
}

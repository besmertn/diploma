import { Component, OnInit } from '@angular/core';
import {User} from "../user.model";
import {AuthenticationService} from "../authentication.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  currentUser: User;
  apptitle: string = 'Diploma';

  constructor(
        private router: Router,
        private authenticationService: AuthenticationService
    ) {
        this.authenticationService.currentUser.subscribe(x => this.currentUser = x);
    }

  ngOnInit(): void {
  }

   logout() {
        this.authenticationService.logout();
        this.router.navigate(['/login']);
    }
}


export class User {
  constructor(
    public id: number,
    public username: string,
    public email: string,
    public passwordHash: string
  ) {}
}

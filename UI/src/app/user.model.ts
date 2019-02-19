
export class User {
  public token?: string;
  constructor(
    public id: number,
    public username: string,
    public email: string,
    public passwordHash: string,
  ) {}
}

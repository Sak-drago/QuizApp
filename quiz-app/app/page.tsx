import { redirect } from "next/navigation";

export default function Home(){
  //redirecting to auth when the website is opened.
  redirect("/auth/login");
}
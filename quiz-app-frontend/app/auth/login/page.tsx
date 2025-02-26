"use client"
import type React from "react"
import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { LogIn } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function LoginPage() {
  const router = useRouter()
  const [role, setRole] = useState("user")
  const [title, setTitle] = useState("Welcome back to Sparkl User")

  useEffect(() => {
  const changeTitle  = role === "admin" ? "Welcome back to Sparkl CMS Admin" : "Welcome back to Sparkl User"
  setTitle(changeTitle)
  document.title = changeTitle;    
  },[role])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    //Temperoray auth right now. JWT to be implemented
    //Plan is to have admin on an entirely different access point
    if (role === "admin") {
      router.push("/admin/dashboard")  
    } else {
      router.push("/user/dashboard")
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-background p-4 space-y-4">
    <h1 className="text-4xl font-bold text-center">{title}</h1>
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold">Login</CardTitle>
          <CardDescription>Enter your credentials to access the quiz platform</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" placeholder="userOfGoodEdTech@sparkl.com" required /> {/* Compulsory field */}
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" required /> {/* Compulsory field */}
            </div>
            <div className="space-y-2">
              <Label>Role</Label> 
              <RadioGroup defaultValue="user" onValueChange={setRole} className="flex space-x-4"> {/* Default value is user. Changes on Toggle */}
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="user" id="user" />
                  <Label htmlFor="user">User</Label> 
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="admin" id="admin" />
                  <Label htmlFor="admin">Admin</Label>
                </div>
              </RadioGroup>
            </div>
            <Button type="submit" className="w-full">
              <LogIn className="mr-2 h-4 w-4" />
              Login
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}

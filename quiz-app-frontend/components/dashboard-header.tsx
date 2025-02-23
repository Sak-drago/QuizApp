"use client"

import { LogOut, User } from "lucide-react"
import { useRouter } from "next/navigation"

import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu"
import { Button } from "@/components/ui/button"

interface DashboardHeaderProps {
  username: string
}

export function DashboardHeader({ username }: DashboardHeaderProps) {
  const router = useRouter()

  const handleLogout = () => {
    // Add your logout logic here
    router.push("/auth/login")
  }

  return (
    <header className="border-b">
      <div className="container flex h-16 items-center justify-between px-4">
        <h1 className="text-2xl font-bold">Sparkl Quiz Centre</h1>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="flex items-center space-x-2">
              <User className="h-4 w-4" />
              <span>{username}</span>
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem onClick={handleLogout}>
              <LogOut className="mr-2 h-4 w-4" />
              Logout
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </header>
  )
}
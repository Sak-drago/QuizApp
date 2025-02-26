"use client"

import { DashboardHeader } from "@/components/dashboard-header"
import {Tabs, TabsList, TabsTrigger} from "@/components/ui/tabs"

export default function DashboardPageAdmin() {
  return(
    <div className="min-h-screen bg-background">
    <DashboardHeader username="admin" />
    <main className="container py-4">
      <h2 className="text-2xl font-bold mb-3">Dashboard</h2>
      <Tabs defaultValue ="create" className="space-y-4">
        <TabsList className="grid w-full grid-cols-2 lg:grid-cols-4">
          <TabsTrigger value="create">Create</TabsTrigger>
          <TabsTrigger value="quizzes">Quizzes</TabsTrigger>
          <TabsTrigger value="questions">Questions</TabsTrigger>
          <TabsTrigger value="results">Report</TabsTrigger>
        </TabsList>
      </Tabs>
    </main>
    </div>
  )
}

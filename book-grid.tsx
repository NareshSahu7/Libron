"use client"

import type { Book } from "@/lib/types"
import { BookCard } from "@/components/library/book-card"
import { Skeleton } from "@/components/ui/skeleton"

const GRID_CLASS =
  "grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5"

export function BookGridSkeleton({ count = 15 }: { count?: number }) {
  return (
    <div className={GRID_CLASS}>
      {Array.from({ length: count }).map((_, i) => (
        <div key={i} className="flex flex-col gap-2 overflow-hidden rounded-xl border border-border/60 bg-card">
          <Skeleton className="aspect-[2/3] w-full rounded-none" />
          <div className="flex flex-col gap-2 p-3">
            <Skeleton className="h-4 w-full" />
            <Skeleton className="h-3 w-2/3" />
          </div>
        </div>
      ))}
    </div>
  )
}

interface BookGridProps {
  books: Book[]
  onSelect: (book: Book) => void
}

export function BookGrid({ books, onSelect }: BookGridProps) {
  return (
    <div className={GRID_CLASS}>
      {books.map((book) => (
        <BookCard key={book.key} book={book} onSelect={onSelect} />
      ))}
    </div>
  )
}

"use client"

import { Star } from "lucide-react"
import type { Book } from "@/lib/types"
import { BookCover } from "@/components/library/book-cover"
import { Badge } from "@/components/ui/badge"

interface BookCardProps {
  book: Book
  onSelect: (book: Book) => void
}

export function BookCard({ book, onSelect }: BookCardProps) {
  return (
    <button
      type="button"
      onClick={() => onSelect(book)}
      className="group flex flex-col overflow-hidden rounded-xl border border-border/60 bg-card text-left transition-all hover:-translate-y-1 hover:border-primary/40 hover:shadow-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
    >
      <div className="relative aspect-[2/3] w-full overflow-hidden bg-muted">
        <BookCover
          coverId={book.coverId}
          title={book.title}
          className="transition-transform duration-300 group-hover:scale-105"
        />
        {book.ratingsAverage ? (
          <Badge className="absolute right-2 top-2 gap-1 bg-background/90 text-foreground shadow-sm backdrop-blur-sm">
            <Star className="size-3 fill-primary text-primary" />
            {book.ratingsAverage.toFixed(1)}
          </Badge>
        ) : null}
      </div>
      <div className="flex flex-1 flex-col gap-1 p-3">
        <h3 className="line-clamp-2 text-sm font-semibold leading-snug text-card-foreground">
          {book.title}
        </h3>
        <p className="line-clamp-1 text-xs text-muted-foreground">
          {book.authors.length > 0 ? book.authors.join(", ") : "Unknown author"}
        </p>
        {book.firstPublishYear ? (
          <p className="mt-auto pt-1 text-xs text-muted-foreground/80">
            {book.firstPublishYear}
          </p>
        ) : null}
      </div>
    </button>
  )
}

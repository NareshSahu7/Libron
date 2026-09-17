"use client"

import useSWR from "swr"
import { Star, BookCopy, FileText, Languages, Calendar, ExternalLink } from "lucide-react"
import type { Book, BookDetail } from "@/lib/types"
import { fetcher } from "@/lib/fetcher"
import { BookCover } from "@/components/library/book-cover"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Skeleton } from "@/components/ui/skeleton"
import { Separator } from "@/components/ui/separator"

interface BookDetailDialogProps {
  book: Book | null
  onClose: () => void
}

function Stat({
  icon: Icon,
  label,
  value,
}: {
  icon: React.ComponentType<{ className?: string }>
  label: string
  value: string
}) {
  return (
    <div className="flex flex-col items-center gap-1 rounded-lg bg-muted/60 p-3 text-center">
      <Icon className="size-4 text-primary" />
      <span className="text-sm font-semibold text-foreground">{value}</span>
      <span className="text-[11px] text-muted-foreground">{label}</span>
    </div>
  )
}

export function BookDetailDialog({ book, onClose }: BookDetailDialogProps) {
  const { data, isLoading } = useSWR<BookDetail>(
    book ? `/api/books/detail?key=${encodeURIComponent(book.key)}` : null,
    fetcher,
  )

  return (
    <Dialog open={book !== null} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="max-h-[90vh] max-w-2xl overflow-y-auto">
        {book && (
          <>
            <DialogHeader className="text-left">
              <DialogTitle className="text-xl leading-tight text-balance">
                {book.title}
              </DialogTitle>
              <DialogDescription>
                {book.authors.length > 0 ? book.authors.join(", ") : "Unknown author"}
              </DialogDescription>
            </DialogHeader>

            <div className="flex flex-col gap-5 sm:flex-row">
              <div className="mx-auto w-40 shrink-0 overflow-hidden rounded-lg border border-border shadow-md sm:mx-0">
                <div className="aspect-[2/3] w-full">
                  <BookCover coverId={book.coverId} title={book.title} size="L" />
                </div>
              </div>

              <div className="flex flex-1 flex-col gap-4">
                <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
                  {book.ratingsAverage ? (
                    <Stat
                      icon={Star}
                      label={`${book.ratingsCount ?? 0} ratings`}
                      value={book.ratingsAverage.toFixed(1)}
                    />
                  ) : null}
                  {book.firstPublishYear ? (
                    <Stat icon={Calendar} label="Published" value={String(book.firstPublishYear)} />
                  ) : null}
                  {book.pages ? (
                    <Stat icon={FileText} label="Pages" value={String(book.pages)} />
                  ) : null}
                  <Stat icon={BookCopy} label="Editions" value={String(book.editionCount)} />
                  {book.languages.length > 0 ? (
                    <Stat
                      icon={Languages}
                      label="Languages"
                      value={book.languages.slice(0, 3).join(", ").toUpperCase()}
                    />
                  ) : null}
                </div>

                <div className="flex flex-col gap-2">
                  <h4 className="text-sm font-semibold text-foreground">About</h4>
                  {isLoading ? (
                    <div className="flex flex-col gap-2">
                      <Skeleton className="h-4 w-full" />
                      <Skeleton className="h-4 w-full" />
                      <Skeleton className="h-4 w-3/4" />
                    </div>
                  ) : data?.description ? (
                    <p className="text-sm leading-relaxed text-muted-foreground">
                      {data.description.split("\n")[0]}
                    </p>
                  ) : (
                    <p className="text-sm text-muted-foreground">
                      No description is available for this title.
                    </p>
                  )}
                </div>
              </div>
            </div>

            {book.subjects.length > 0 && (
              <>
                <Separator />
                <div className="flex flex-col gap-2">
                  <h4 className="text-sm font-semibold text-foreground">Subjects</h4>
                  <div className="flex flex-wrap gap-1.5">
                    {book.subjects.map((subject) => (
                      <Badge key={subject} variant="secondary" className="font-normal">
                        {subject}
                      </Badge>
                    ))}
                  </div>
                </div>
              </>
            )}

            <Button
              nativeButton={false}
              render={
                <a
                  href={`https://openlibrary.org${book.key}`}
                  target="_blank"
                  rel="noopener noreferrer"
                />
              }
              variant="outline"
              className="w-full"
            >
              <ExternalLink data-icon="inline-start" />
              View on Open Library
            </Button>
          </>
        )}
      </DialogContent>
    </Dialog>
  )
}

"use client"

import * as React from "react"
import useSWR from "swr"
import { ChevronLeft, ChevronRight, SearchX, Library, TriangleAlert } from "lucide-react"
import type { Book, SearchResponse } from "@/lib/types"
import { fetcher } from "@/lib/fetcher"
import { SearchBar } from "@/components/library/search-bar"
import { Filters } from "@/components/library/filters"
import { BookGrid, BookGridSkeleton } from "@/components/library/book-grid"
import { BookDetailDialog } from "@/components/library/book-detail-dialog"
import { Button } from "@/components/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"

const MAX_PAGE = 42 // Open Library returns up to ~1000 results.

export function BookFinder() {
  const [query, setQuery] = React.useState("")
  const [subject, setSubject] = React.useState("all")
  const [sort, setSort] = React.useState("relevance")
  const [page, setPage] = React.useState(1)
  const [selected, setSelected] = React.useState<Book | null>(null)

  const params = new URLSearchParams({
    q: query,
    subject,
    sort,
    page: String(page),
  })
  const key = `/api/books?${params.toString()}`

  const { data, error, isLoading } = useSWR<SearchResponse>(key, fetcher, {
    keepPreviousData: true,
    revalidateOnFocus: false,
  })

  function resetAndSet(fn: () => void) {
    fn()
    setPage(1)
  }

  const totalPages = data
    ? Math.min(MAX_PAGE, Math.ceil(data.total / data.perPage))
    : 1

  const heading = query
    ? `Results for "${query}"`
    : subject !== "all"
      ? "Browsing collection"
      : "Popular fiction"

  return (
    <div className="flex flex-col gap-6">
      <div className="flex flex-col gap-4 rounded-2xl border border-border/60 bg-card/60 p-4 shadow-sm sm:p-5">
        <SearchBar onSearch={(v) => resetAndSet(() => setQuery(v))} />
        <Filters
          subject={subject}
          sort={sort}
          onSubjectChange={(v) => resetAndSet(() => setSubject(v))}
          onSortChange={(v) => resetAndSet(() => setSort(v))}
        />
      </div>

      <div className="flex items-baseline justify-between gap-4">
        <h2 className="text-lg font-semibold tracking-tight">{heading}</h2>
        {data && data.total > 0 && (
          <span className="shrink-0 text-sm text-muted-foreground">
            {data.total.toLocaleString()} books
          </span>
        )}
      </div>

      {error ? (
        <Empty className="border">
          <EmptyHeader>
            <EmptyMedia variant="icon">
              <TriangleAlert />
            </EmptyMedia>
            <EmptyTitle>Something went wrong</EmptyTitle>
            <EmptyDescription>
              We couldn&apos;t reach the library right now. Please try again.
            </EmptyDescription>
          </EmptyHeader>
        </Empty>
      ) : isLoading && !data ? (
        <BookGridSkeleton />
      ) : data && data.books.length === 0 ? (
        <Empty className="border">
          <EmptyHeader>
            <EmptyMedia variant="icon">
              <SearchX />
            </EmptyMedia>
            <EmptyTitle>No books found</EmptyTitle>
            <EmptyDescription>
              Try a different search term or adjust your filters.
            </EmptyDescription>
          </EmptyHeader>
          <EmptyContent>
            <Button
              variant="outline"
              onClick={() => {
                setQuery("")
                setSubject("all")
                setSort("relevance")
                setPage(1)
              }}
            >
              <Library data-icon="inline-start" />
              Reset search
            </Button>
          </EmptyContent>
        </Empty>
      ) : data ? (
        <div className="flex flex-col gap-6" data-loading={isLoading}>
          <div className="transition-opacity data-[loading=true]:opacity-60" data-loading={isLoading}>
            <BookGrid books={data.books} onSelect={setSelected} />
          </div>

          {totalPages > 1 && (
            <div className="flex items-center justify-center gap-4">
              <Button
                variant="outline"
                size="sm"
                disabled={page <= 1 || isLoading}
                onClick={() => setPage((p) => Math.max(1, p - 1))}
              >
                <ChevronLeft data-icon="inline-start" />
                Previous
              </Button>
              <span className="text-sm text-muted-foreground">
                Page {page} of {totalPages}
              </span>
              <Button
                variant="outline"
                size="sm"
                disabled={page >= totalPages || isLoading}
                onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
              >
                Next
                <ChevronRight data-icon="inline-end" />
              </Button>
            </div>
          )}
        </div>
      ) : null}

      <BookDetailDialog book={selected} onClose={() => setSelected(null)} />
    </div>
  )
}

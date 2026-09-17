import { SiteHeader } from "@/components/library/site-header"
import { BookFinder } from "@/components/library/book-finder"

export default function Page() {
  return (
    <div className="flex min-h-screen flex-col bg-background">
      <SiteHeader />
      <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-8 sm:px-6 sm:py-10">
        <section className="mb-8 flex flex-col items-center gap-3 text-center">
          <span className="rounded-full border border-border/60 bg-card px-3 py-1 text-xs font-medium text-muted-foreground">
            Powered by Open Library
          </span>
          <h1 className="max-w-2xl text-3xl font-bold tracking-tight text-balance sm:text-4xl">
            Find your next great read
          </h1>
          <p className="max-w-xl text-pretty text-muted-foreground">
            Search millions of books by title, author, or subject. Explore
            covers, ratings, and details from libraries around the world.
          </p>
        </section>
        <BookFinder />
      </main>
      <footer className="border-t border-border/60 py-6">
        <div className="mx-auto max-w-6xl px-4 text-center text-sm text-muted-foreground sm:px-6">
          Book data provided by the{" "}
          <a
            href="https://openlibrary.org"
            target="_blank"
            rel="noopener noreferrer"
            className="font-medium text-foreground underline underline-offset-4"
          >
            Open Library
          </a>{" "}
          project.
        </div>
      </footer>
    </div>
  )
}

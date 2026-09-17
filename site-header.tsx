import { BookOpenText } from "lucide-react"

export function SiteHeader() {
  return (
    <header className="border-b border-border/60 bg-card/50 backdrop-blur-sm">
      <div className="mx-auto flex max-w-6xl items-center gap-3 px-4 py-4 sm:px-6">
        <div className="flex size-10 items-center justify-center rounded-xl bg-primary text-primary-foreground">
          <BookOpenText className="size-5" />
        </div>
        <div className="flex flex-col">
          <span className="text-base font-semibold leading-tight tracking-tight">
            Stacks
          </span>
          <span className="text-xs text-muted-foreground">
            Library Book Finder
          </span>
        </div>
      </div>
    </header>
  )
}

"use client"

import * as React from "react"
import { BookMarked } from "lucide-react"
import { cn } from "@/lib/utils"
import { coverUrl } from "@/lib/types"

interface BookCoverProps {
  coverId: number | null
  title: string
  size?: "M" | "L"
  className?: string
}

export function BookCover({ coverId, title, size = "M", className }: BookCoverProps) {
  const [failed, setFailed] = React.useState(false)
  const url = coverUrl(coverId, size)

  if (!url || failed) {
    return (
      <div
        className={cn(
          "flex flex-col items-center justify-center gap-2 bg-gradient-to-br from-accent to-secondary p-4 text-center",
          className,
        )}
      >
        <BookMarked className="size-6 text-primary/60" />
        <span className="line-clamp-4 text-xs font-medium text-muted-foreground">
          {title}
        </span>
      </div>
    )
  }

  return (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      src={url || "/placeholder.svg"}
      alt={`Cover of ${title}`}
      loading="lazy"
      onError={() => setFailed(true)}
      className={cn("size-full object-cover", className)}
    />
  )
}

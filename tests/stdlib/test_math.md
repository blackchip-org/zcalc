# math

## +

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `+`              | `8`

## add

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `add`            | `8`

## -

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `-`              | `4`

## sub

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `sub`            | `4`

## *

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `*`              | `12`

## mul

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `mul`            | `12`

## /

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `/`              | `3`

## div

| Input            | Stack
|------------------|-------------|
| `6`              | `6`
| `2`              | `6 ; 2`
| `div`            | `3`

## %

| Input            | Stack
|------------------|-------------|
| `3`              | `3`
| `2`              | `3 ; 2`
| `%`              | `1`

## is decimal

If floating point, it would be 3.3000000000000003

| Input            | Stack
|------------------|-------------|
| `1.1`            | `1.1`
| `2.2`            | `1.1 ; 2.2`
| `a`              | `3.3`

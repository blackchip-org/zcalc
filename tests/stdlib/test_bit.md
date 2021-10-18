# bit

## &

| Input       | Stack
|-------------|-------------|
| `0x88`      | `0x88`
| `0xf0`      | `0x88 ; 0xf0`
| `& ; hex`   | `0x80`

## dec

| Input       | Stack
|-------------|-------------|
| `0x0f`      | `0x0f`
| `dec`       | `15`

## <<

| Input        | Stack
|--------------|-------------|
| `32`         | `32`
| `1`          | `32 ; 1`
| `<<`         | `64`

## shl

| Input        | Stack
|--------------|-------------|
| `32`         | `32`
| `1`          | `32 ; 1`
| `shl`        | `64`

## >>

| Input         | Stack
|---------------|-------------|
| `64`          | `64`
| `1`           | `64 ; 1`
| `>>`          | `32`

## shr

| Input         | Stack
|---------------|-------------|
| `64`          | `64`
| `1`           | `64 ; 1`
| `shr`         | `32`

## ^

| Input       | Stack
|-------------|-------------|
| `0x0f`      | `0x0f`
| `0xff`      | `0x0f ; 0xff`
| `^ ; hex`   | `0xf0`
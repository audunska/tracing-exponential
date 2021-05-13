pub async fn f0() -> Result<(), String> {
    f1().await
}
pub async fn f1() -> Result<(), String> {
    f2().await
}
pub async fn f2() -> Result<(), String> {
    f3().await
}
pub async fn f3() -> Result<(), String> {
    f4().await
}
pub async fn f4() -> Result<(), String> {
    f5().await
}
pub async fn f5() -> Result<(), String> {
    f6().await
}
pub async fn f6() -> Result<(), String> {
    f7().await
}
pub async fn f7() -> Result<(), String> {
    f8().await
}
pub async fn f8() -> Result<(), String> {
    f9().await
}
pub async fn f9() -> Result<(), String> {
    f10().await
}

pub async fn f10() -> Result<(), String> {
    Ok(())
}

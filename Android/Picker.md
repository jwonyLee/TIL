[이 글](https://developer.android.com/guide/topics/ui/controls/pickers?authuser=1)을 기반으로 번역기(구글, 파파고, 카카오)를 참고하여 작성하였습니다. 

안드로이드는 사용자가 시간을 선택하거나 날짜를 사용할 수 있는 대화 상자로 선택할 수 있는 컨트롤을 제공한다. 각 `Picker`는 시간 (시, 분, 오전 / 오후) 또는 날짜 (월, 일, 년)의 부분을 선택하는 컨트롤을 제공한다. 이렇게 `Picker`를 사용하면 사용자가 유효하고, 형식이 정확하며, 사용자  지역에 맞게 조정된 시간 또는 날짜를 선택할 수 있다.

Android Developer에서는 `DialogFragment`를 사용할 것을 권고한다. `DialogFragment`는 `Dialog`의 생명 주기를 관리하며, 단말기의 기본 `dialog` 또는 큰 화면의 레이아웃에 포함한 부분과 같이 다양한 레이아웃 구성으로 `Picker`를 표시할 수 있다.[^1]

`DialogFragment`는 Android 3.0(API 레벨 11) 때 처음 추가되었지만, Android 1.6보다 낮은 버전의 Android를 지원하는 경우에는 Support Library에서 `DialogFragment `클래스를 사용하여 이전 버전과의 호환성을 지원할 수 있다.



## Time Picker 만들기

`DialogFragment`를 사용하여 `TimePickerDialog`를 표시하려면 `DialogFragment`를 상속받는 프래그먼트를 만들고, `TimePickerDialog`를 반환하는 `onClreateDialog()` 메소드를 정의해야 한다.

### Time Picker를 위한 `DialogFragment` 상속[^2]

`TimePickerDialog`를 위한 `DialogFragment`를 정의하려면 다음과 같다.

- `onCreateDialog()` 메소드를 정의한다. 이 메소드는 `TimePickerDialog`의 인스턴스를 반환한다.
- `TimePickerDialog.OnTimeSetListener` 인터페이스를 구현하여 사용자가 시간을 설정할 때 콜백[^3]을 수신한다.

예제 코드(Kotlin):

```Kotlin
class TimePickerFragment : DialogFragment(), TimePickerDialog.OnTimeSetListener {

    override fun onCreateDialog(savedInstanceState: Bundle): Dialog {
        // Use the current time as the default values for the picker
        val c = Calendar.getInstance()
        val hour = c.get(Calendar.HOUR_OF_DAY)
        val minute = c.get(Calendar.MINUTE)

        // Create a new instance of TimePickerDialog and return it
        return TimePickerDialog(activity, this, hour, minute, DateFormat.is24HourFormat(activity))
    }

    override fun onTimeSet(view: TimePicker, hourOfDay: Int, minute: Int) {
        // Do something with the time chosen by the user
    }
}
```

생성자 인수에 대한 자세한 내용은 [`TimePickerDialog`](https://developer.android.com/reference/android/app/TimePickerDialog.html?authuser=1) 클래스를 참조.

이제 프래그먼트의 인스턴스를 당신의 액티비티에 이벤트를 추가하면 된다.[^4]

### Time Picker 보여주기

위에 표시된 것과 같은 `DialogFragment`를 정의한 후에는 `DialogFragment` 인스턴스를 만들고 `show()` 메소드를 호출하여 Time Picker를 표시할 수 있다.

아래의 코드는 클릭하면 `Dialog`를 표시하는 메소드를 호출하는 버튼이다.[^5]

```xml
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/pick_time"
    android:onClick="showTimePickerDialog" />
```

사용자가 이 버튼을 클릭할 때, 시스템은 다음 메소드를 호출한다.

```Kotlin
fun showTimePickerDialog(v: View) {
    TimePickerFragment().show(supportFragmentManager, "timePicker")
}
```

이 메소드는 위에 정의된 `DialogFragment`의 새 인스턴에 대한 `show()` 메소드를 호출한다. `show()` 메소드에서는 `FragmentManager` 인스턴스와 `Fragment`에 대한 고유한 태그 이름이 필요하다.
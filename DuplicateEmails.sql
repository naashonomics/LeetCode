select distinct `Email` from `Person` group by `Email` Having Count(`Email`) > 1;
